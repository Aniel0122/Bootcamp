public class Ejecicio3 {

    public static void main(String[] args) {
        // Llamando a la función sumaTresNumeros y mostrando el resultado
        int resultado = sumaTresNumeros(0, 0, 0);
        System.out.println("El resultado es: " + resultado);

        // Creando un objeto de la clase Coche y agregando una puerta

        Coche miCoche = new Coche();
        miCoche.agregarPuerta();
        System.out.println("Mi coche tiene " + miCoche.getNumPuertas() + " puertas.");
    }
    public static int sumaTresNumeros(int num1, int num2, int num3) {
        return num1 + num2 + num3;
    }
    public static class Coche {
        private int numPuertas;
        public void agregarPuerta() {
            numPuertas++;
        }
        public int getNumPuertas() {
            return numPuertas;
        }
    }

}