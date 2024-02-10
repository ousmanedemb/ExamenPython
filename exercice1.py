import numpy as np
import matplotlib.pyplot as plt

# Définition des paramètres
debut = 0
fin = 1
nbr_points = 5432


# Définition de la fonction
def f(x):
    return x ** 5


# Tracé de la courbe
x_values = np.linspace(debut, fin, 100)
y_values = f(x_values) + 0.5
plt.plot(x_values, y_values, label='Courbe x^5', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tracé de la courbe x^5')
plt.grid(True)
plt.legend()

# Tracé du carré délimité par les droites: x=0, x=1, y=0, y=1
plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color='black')

# Génération de points aléatoires
x_points = np.random.uniform(debut, fin, nbr_points)
y_points = np.random.uniform(0, f(fin), nbr_points)

# Tracé des points
for x, y in zip(x_points, y_points):
    if y > f(x) + 0.5:
        plt.plot(x, y, 'b+', markersize=5)
    else:
        plt.plot(x, y, 'go', markersize=5)

plt.show()
