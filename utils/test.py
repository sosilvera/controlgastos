import graphics as gh

consumos = [
    {
        "periodo": 16,
        "descripcion": "Abril",
        "monto": "Silla Bebe",
        "banco": 1986.0
    },
    {
        "periodo": 197,
        "descripcion": "Abril",
        "monto": "Mantenimiento Cuenta",
        "banco": 1325.0
    },
    {
        "periodo": 175,
        "descripcion": "Abril",
        "monto": "Passline",
        "banco": 2843.0
    },
    {
        "periodo": 176,
        "descripcion": "Mayo",
        "monto": "Passline",
        "banco": 2843.0
    },
    {
        "periodo": 186,
        "descripcion": "Mayo",
        "monto": "Passline 2",
        "banco": 7961.0
    },
    {
        "periodo": 172,
        "descripcion": "Mayo",
        "monto": "Grupo Mobilesa",
        "banco": 8565.0
    },
    {
        "periodo": 18,
        "descripcion": "Junio",
        "monto": "Silla Bebe",
        "banco": 1986.0
    },
    {
        "periodo": 29,
        "descripcion": "Junio",
        "monto": "Auriculares HP",
        "banco": 1248.0
    },
    {
        "periodo": 33,
        "descripcion": "Junio",
        "monto": "Prestamo 1",
        "banco": 7945.0
    },
    {
        "periodo": 25,
        "descripcion": "Junio",
        "monto": "Calza Corta",
        "banco": 731.0
    }
]

gh.plot_evolucion_gastos(consumos)
# Abril: 6154
# Mayo: 19099
# Junio: 11950