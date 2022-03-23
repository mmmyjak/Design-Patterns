using System;

namespace prototype
{
    public class Osoba
    {
        public string Imie;
        public int Wiek;
        public int Id;

        public Osoba Kopia()
        {
            return (Osoba) this.MemberwiseClone();
        }

        public override string ToString()
        {
            return Imie + " wiek: " + Wiek + " , ID: " + Id;
        }


    }
    class Program
    {
        static void Main(string[] args)
        {
            Osoba nr1 = new Osoba();
            nr1.Imie = "Marek";
            nr1.Wiek = 32;
            nr1.Id = 0;

            Osoba nr2 = nr1.Kopia();

            Console.WriteLine(nr1);
            Console.WriteLine(nr2);

           
            nr2.Imie = "Franek";
            nr2.Wiek = 29;
            nr2.Id = 1;
            Console.WriteLine("Po zmianie:");
            Console.WriteLine(nr1);
            Console.WriteLine(nr2);
        }
    }
}
