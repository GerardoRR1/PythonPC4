-- Crear la tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    fecha DATE,
    producto TEXT,
    cantidad INTEGER,
    precio_unitario REAL
);

-- Crear la tabla de tipo_cambio
CREATE TABLE IF NOT EXISTS tipo_cambio (
    fecha DATE,
    tipo_cambio REAL
);
