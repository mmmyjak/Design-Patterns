using System;

namespace ConsoleApp1
{
    public interface IBuilder
    {
        void Procesor_IntelCoreI5();
        void Procesor_AMDRyzen7();
        void KartaGraficzna_GeforceRTX3060();
        void KartaGraficzna_Radeon();
        void RAM32GB();
        void RAM16GB();
        void RAM8GB();

    }

    public class ConcreteBuilder : IBuilder
    {
        private Komputer _komp = new Komputer();

        public ConcreteBuilder()
        {
            this.Reset();
        }

        public void Reset()
        {
            this._komp = new Komputer();
        }

        public void Procesor_IntelCoreI5()
        {
            this._komp.DodajProcesor("Procesor IntelCoreI5 - 649PLN");
        }
        public void Procesor_AMDRyzen7()
        {
            this._komp.DodajProcesor("Procesor AMD Ryzen 7 - 1839PLN");
        }
        public void KartaGraficzna_GeforceRTX3060()
        {
            this._komp.DodajKarte("Geforce RTX 3060 - 3499PLN");
        }
        public void KartaGraficzna_Radeon()
        {
            this._komp.DodajKarte("HP Radeon R7 - 850PLN");
        }
        public void RAM32GB()
        {
            this._komp.DodajPamiec("RAM 32GB - 739PLN");
        }
        public void RAM16GB()
        {
            this._komp.DodajPamiec("RAM 16GB - 349PLN");
        }
        public void RAM8GB()
        {
            this._komp.DodajPamiec("RAM 8GB - 149PLN");
        }

        public Komputer Sklad()
        {
            Komputer result = this._komp;
            return result;
        }
    }


    public class Komputer
    {
        string procesor = "";
        string kartaGraficzna = "";
        string pamiec = "";

        public void DodajProcesor(string proc)
        {
            this.procesor = "Procesor: " + proc;
        }

        public void DodajKarte(string karta)
        {
            this.kartaGraficzna = "Karta graficzna: " + karta;
        }

        public void DodajPamiec(string pam)
        {
            this.pamiec = "Pamięć: " + pam;
        }

        public string Budowa()
        {
            return this.kartaGraficzna + ", " + this.procesor + ", " + this.pamiec;
        }
    }

    public class Director
    {
        private IBuilder _builder;
        public IBuilder Builder
        {
            set { _builder = value; }
        }

        public void ZłóżKomputerDoGier()
        {
            this._builder.Procesor_AMDRyzen7();
            this._builder.RAM32GB();
            this._builder.KartaGraficzna_GeforceRTX3060();
        }
        public void ZłóżKomputerDoBiura()
        {
            this._builder.Procesor_AMDRyzen7();
            this._builder.RAM16GB();
            this._builder.KartaGraficzna_Radeon();

        }
        public void ZłóżKomputerDoDomu()
        {
            this._builder.KartaGraficzna_Radeon();
            this._builder.RAM8GB();
            this._builder.Procesor_IntelCoreI5();
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            var director = new Director();
            var builder = new ConcreteBuilder();
            director.Builder = builder;

            Console.WriteLine("Wybierz opcję: 1) Komputer do biura 2) Komputer do gier 3)Komputer do domu");
            string opcja = Console.ReadLine();
            if (opcja == "1")
            {
                director.ZłóżKomputerDoBiura();
                Console.WriteLine("Komputer Do Biura:");
                Console.WriteLine(builder.Sklad().Budowa());
            }
            else if (opcja == "2")
            {
                director.ZłóżKomputerDoGier();
                Console.WriteLine("Komputer Do Gier:");
                Console.WriteLine(builder.Sklad().Budowa());
            }
            else if (opcja == "3")
            {
                director.ZłóżKomputerDoDomu();
                Console.WriteLine("Komputer Do Domu:");
                Console.WriteLine(builder.Sklad().Budowa());
            }
            else Console.WriteLine("Zła OPCJA");


            Console.ReadKey();
        }
    }
}
