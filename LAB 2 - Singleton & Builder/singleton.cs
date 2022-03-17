using System;

namespace singleton
{
    public sealed class Singleton
    {
        private Singleton() { }

        private static Singleton _instance;

        public static Singleton GetInstance()
        {
            if (_instance == null)
            {
                _instance = new Singleton();
            }
            return _instance;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Singleton sin1 = Singleton.GetInstance();
            Singleton sin2 = Singleton.GetInstance();
            Console.WriteLine(sin1 == sin2);

        }
    }
}
