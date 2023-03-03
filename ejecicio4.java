public class ejecicio4 {
    public static void main(String[] args) {
        // If
        int numeroIf = 10;
        if (numeroIf > 0) {
            System.out.println("El número es positivo");
        } else if (numeroIf < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número es 0");
        }

        // While
        int numeroWhile = 0;
        while (numeroWhile < 5) {
            numeroWhile++;
            System.out.println(numeroWhile);
        }

        // Do While
        int numeroDoWhile = 0;
        do {
            numeroDoWhile++;
            System.out.println(numeroDoWhile);
        } while (numeroDoWhile < 5);

        // For
        for (int numeroFor = 0; numeroFor <= 5; numeroFor++) {
            System.out.println(numeroFor);
        }

        // Estación del año (sin Switch)
        String estacion = "verano";
        if (estacion.equals("primavera")) {
            System.out.println("Estamos en primavera");
        } else if (estacion.equals("verano")) {
            System.out.println("Estamos en verano");
        } else if (estacion.equals("otoño")) {
            System.out.println("Estamos en otoño");
        } else if (estacion.equals("invierno")) {
            System.out.println("Estamos en invierno");
        } else {
            System.out.println("La variable estacion no es una estación del año");
        }
    }
}
