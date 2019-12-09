using System;
using System.IO;

namespace _1
{
    class Program {
		static void Main(string[] args) {
			string input = System.IO.File.ReadAllText(@"./input.txt");
			Console.Write(input);
		}
	}
}
