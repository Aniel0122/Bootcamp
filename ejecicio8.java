public class ejecicio8 {

    public static void main(String[] args) {

        Persona persona = new Persona();
        persona.setnombre("Aniel");

        System.out.println("Mi puede ser " + persona.getnombre());
        persona.setedad(20);

        System.out.println("Ahora mismo tengo " + persona.getedad() + " años de edad");
        persona.settelefono(829280119);

        System.out.println("Mi teléfono es " + persona.gettelefono());
    }
}

class Persona{
    private String nombre;
    private int edad;
    private int telefono;

    public void setnombre(String nombre) {
        this.nombre = nombre;
    }

    public String getnombre() {
        return nombre;
    }

    public void setedad(int edad){
        this.edad = edad;
    }

    public int getedad() {
        return edad;
    }

    public void settelefono(int telefono){
        this.telefono = telefono;
    }

    public int gettelefono() {
        return telefono;
    }
}