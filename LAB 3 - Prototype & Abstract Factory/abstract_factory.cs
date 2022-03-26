using System;

namespace abstractfactory
{
    public interface IAbstractFactory
    {
        IAbstractKoszulka CreateKoszulka();
        IAbstractSpodnie CreateSpodnie();
        IAbstractButy CreateButy();
    }
    class WinterFactory : IAbstractFactory
    {
        public IAbstractKoszulka CreateKoszulka()
        {
            return new KoszulkaZDługimRękawem();
        }
        public IAbstractSpodnie CreateSpodnie()
        {
            return new DługieSpodnie();
        }
        public IAbstractButy CreateButy()
        {
            return new ButyZimowe();
        }
    }

    class SummerFactory : IAbstractFactory
    {
        public IAbstractKoszulka CreateKoszulka()
        {
            return new KoszulkaZKrótkimRękawem();
        }
        public IAbstractSpodnie CreateSpodnie()
        {
            return new KrótkieSpodenki();
        }
        public IAbstractButy CreateButy()
        {
            return new Sandały();
        }
    }

    public interface IAbstractKoszulka
    {
        string OpisKoszulki();
    }

    class KoszulkaZDługimRękawem : IAbstractKoszulka
    {
        public string OpisKoszulki()
        {
            return "Koszulka z Długim Rękawem";
        }
    }

    class KoszulkaZKrótkimRękawem : IAbstractKoszulka
    {
        public string OpisKoszulki()
        {
            return "Koszulka z Krótkim Rękawem";
        }
    }
    public interface IAbstractSpodnie
    {
        string OpisSpodni();
    }

    class DługieSpodnie : IAbstractSpodnie
    {
        public string OpisSpodni()
        {
            return "Długie Spodnie";
        }
    }

    class KrótkieSpodenki : IAbstractSpodnie
    {
        public string OpisSpodni()
        {
            return "Krótkie Spodenki";
        }
    }
    public interface IAbstractButy
    {
        string OpisButów();
    }
    class Sandały : IAbstractButy
    {
        public string OpisButów()
        {
            return "Sandały";
        }
    }

    class ButyZimowe : IAbstractButy
    {
        public string OpisButów()
        {
            return "Buty Zimowe";
        }
    }

    class Client
    {
        public void ClientMethod(IAbstractFactory fabryka)
        {
            var spodnie = fabryka.CreateSpodnie();
            var koszula = fabryka.CreateKoszulka();
            var buty = fabryka.CreateButy();

            Console.WriteLine(spodnie.OpisSpodni());
            Console.WriteLine(koszula.OpisKoszulki());
            Console.WriteLine(buty.OpisButów());
        }

        public void Main()
        {
            Console.WriteLine("Summer Factory:");
            ClientMethod(new SummerFactory());

            Console.WriteLine();

            Console.WriteLine("Winter Factory:");
            ClientMethod(new WinterFactory());

        }
    }

    class Program
    {
       
        static void Main(string[] args)
        {
            new Client().Main();
            Console.ReadKey();
        }
    }
}
