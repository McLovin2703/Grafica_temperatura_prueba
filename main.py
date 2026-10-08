import matplotlib.pyplot as plt

años = [2000]

ANGRA_DO_HEROISMO_2000 = {

    "Enero": 13.3,
    "Febrero": 14.8,
    "Marzo": 15,
    "Abril": 13.8,
    "Mayo": 15.8,
    "Junio": 18.7,
    "Julio": 19.6,
    "Agosto": 21.3,
    "Septiembre": 21.1,
    "Octubre": 19.5,
    "Noviembre": 17.9,
    "Diciembre":  14.4,

}

plt.plot(
    ANGRA_DO_HEROISMO_2000.keys(),
    ANGRA_DO_HEROISMO_2000.values()
)

plt.xlabel("Mes")
plt.ylabel("Temperatura °C de ANGRA DO HEROISMO/PORTUGAL")
plt.title("Temperatura durante el año 2000")

plt.show()

