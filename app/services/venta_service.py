from app.repositories.venta_repo import VentaRepository
from app.repositories.producto_repo import ProductoRepository
from app.models.venta import Venta
from app.models.detalle_venta import DetalleVenta
from app.models.movimiento_inventario import MovimientoInventario
from datetime import datetime

class VentaService:

    def __init__(self, db):
        self.db = db
        self.repo = VentaRepository(db)
        self.producto_repo = ProductoRepository(db)

    
    def crear(self, venta_data):

        venta = Venta(
            metodo_pago=venta_data.metodo_pago,
            id_cliente=venta_data.id_cliente,
            estado="ACTIVA",
            fecha=datetime.utcnow()   
        )

        total = 0  

        for d in venta_data.detalles:
            subtotal = (d.precio_unitario * d.cantidad) - d.descuento
            total += subtotal

            detalle = DetalleVenta(
                sku_producto=d.sku_producto,
                cantidad=d.cantidad,
                precio_unitario=d.precio_unitario,
                descuento=d.descuento
            )
            venta.detalles.append(detalle)

            movimiento = MovimientoInventario(
                tipo_movimiento="SALIDA",
                sku_producto=d.sku_producto,
                cantidad=d.cantidad
            )
            self.db.add(movimiento)

            producto = self.producto_repo.obtener_por_sku(d.sku_producto)
            producto.stock_actual -= d.cantidad

        venta.total_venta = total              
        venta.impuestos = round(total * 0.12, 2)  

        self.repo.crear(venta)
        self.db.commit()
        self.db.refresh(venta)

        return venta