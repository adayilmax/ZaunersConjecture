import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_zauner_vectors():
    """Generate specific Zauner vectors for d = 2."""
    vectors = [
        np.array([1, 0]),  # |ψ1⟩ = |0⟩
        np.array([1/np.sqrt(3), np.sqrt(2/3)]),  # |ψ2⟩
        np.array([1/np.sqrt(3), np.sqrt(2/3) * np.exp(2j * np.pi / 3)]),  # |ψ3⟩
        np.array([1/np.sqrt(3), np.sqrt(2/3) * np.exp(4j * np.pi / 3)])  # |ψ4⟩
    ]
    return vectors

def plot_vectors_on_sphere(vectors):
    """Plot vectors on the Bloch sphere to visualize Zauner's conjecture."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vec in vectors:
        alpha, beta = vec
        x = 2 * np.real(np.conj(alpha) * beta)
        y = 2 * np.imag(np.conj(alpha) * beta)
        z = np.abs(alpha)**2 - np.abs(beta)**2
        # Plot lines from origin to the points
        ax.plot([0, x], [0, y], [0, z], 'b-', linewidth=2)

    # Draw the sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="r", alpha=0.1)

    # Set the view angle for better visibility
    ax.view_init(elev=20, azim=135)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Zauner\'s Conjecture Vectors on the Bloch Sphere')
    plt.show()

# Generate and plot vectors
vectors = generate_zauner_vectors()
plot_vectors_on_sphere(vectors)
