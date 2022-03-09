using System;

namespace ConsoleApp1
{
    public interface IProduct
    {
        string Platnosc();
    }

    class PayPal : IProduct
    {
        public string Platnosc()
        {
            return "Klient płaci Paypalem";
        }
    }

    class Blik : IProduct
    {
        public string Platnosc()
        {
            return "Klient płaci Blikiem";
        }
    }
    abstract class Sklep
    {
        public abstract IProduct FactoryMethod();

        public string Dzialanie()
        {
            var product = FactoryMethod();
            var result = "Wynik: " + product.Platnosc();

            return result;
        }
    }

    class PlatnoscPaypalem: Sklep
    {
        public override IProduct FactoryMethod()
        {
            return new PayPal();
        }
    }

    class PlatnoscBlikiem : Sklep
    {
        public override IProduct FactoryMethod()
        {
            return new Blik();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Sklep pl = new PlatnoscPaypalem();
            Console.WriteLine(pl.Dzialanie()); 
            Console.ReadKey();
        }
    }
}
