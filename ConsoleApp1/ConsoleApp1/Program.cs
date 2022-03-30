using System;

namespace ConsoleApp1
{
    class Adaptee
    {    
        public double Delta(double a, double b, double c)
        {
            return b * b - 4 * a * c;
        }

        public void Pierwiastki(double delta, double a, double b)
        {
            delta = Math.Sqrt(delta);
            double x1 = (-b - delta) / 2 * a;
            double x2 = (-b + delta) / 2 * a;
            if (x1 == x2) Console.WriteLine($"Pierwiastek równania {x1}");
            else Console.WriteLine($"Pierwiastki równania: {x1}, {x2}");
        }
    }

    class Adapter
    {
        private readonly Adaptee _adaptee;

        public Adapter(Adaptee adaptee)
        {
            this._adaptee = adaptee;
        }

        public void Rozwiazanie(string dzialanie)
        {
            double a = Convert.ToDouble(Convert.ToString(dzialanie[0]));
            double b = Convert.ToDouble(Convert.ToString(dzialanie[5]));
            double c = Convert.ToDouble(Convert.ToString(dzialanie[8]));
            double delta = _adaptee.Delta(a, b, c);

            _adaptee.Pierwiastki(delta, a, b);

        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Adaptee adaptee = new Adaptee();
            Adapter adapter = new Adapter(adaptee);
            adapter.Rozwiazanie("2x^2+9x+2");

           
        }
    }
}
