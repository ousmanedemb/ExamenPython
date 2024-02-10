import numpy as np
import matplotlib.pyplot as plt


class Courbe:
    def __init__(self, debut, fin, nbr_points=5432):
        self.debut = debut
        self.fin = fin
        self.nbr_points = nbr_points

    def __f(self, x):
        return x ** 5

    def tracer_courbe(self):
        x_valeurs = np.linspace(self.debut, self.fin, 100)
        y_valeurs = self.__f(x_valeurs) + 0.5
        plt.plot(x_valeurs, y_valeurs, label='Courbe x^5', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Tracé de la courbe x^5')
        plt.grid(True)
        plt.legend()

    def au_dessus_ou_en_dessous(self, x, y):
        if y > self.__f(x) + 0.5:
            print("Point est au-dessus de la courbe")
        elif y < self.__f(x) + 0.5:
            print("Point est en dessous de la courbe")
        else:
            print("Point est sur la courbe")

    def generer_points(self):
        x_valeurs = np.random.uniform(self.debut, self.fin, self.nbr_points)
        y_valeurs = np.random.uniform(0, self.__f(self.fin), self.nbr_points)

        for x, y in zip(x_valeurs, y_valeurs):
            if y > self.__f(x) + 0.5:
                plt.plot(x, y, 'b+', markersize=5)
            else:
                plt.plot(x, y, 'go', markersize=5)

        self.tracer_courbe()

        plt.show()


# Exemple d'utilisation
courbe = Courbe(0, 1)
courbe.generer_points()
