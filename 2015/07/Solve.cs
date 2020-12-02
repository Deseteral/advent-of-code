// compile using `mcs ./Solve.cs` and run using `mono ./Solve.exe`

using System;
using System.IO;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;

public class VM {
    public Dictionary<string, ushort> registers;

    Regex immediateValueRegex = new Regex(@"^(\d)+$", RegexOptions.Singleline);
    Regex operatorRegex = new Regex(@"^(.+) (\w+) (.+)$", RegexOptions.Singleline);
    Regex notOperatorRegex = new Regex(@"^NOT (.)+$", RegexOptions.Singleline);

    public VM() {
        this.registers = new Dictionary<string, ushort>();
    }

    public void run(string[] instructions) {
        foreach (string line in instructions) {
            var ss = line.Split(" -> ");
            var lhs = ss[0];
            var target = ss[1];

            // Console.WriteLine(lhs);
            if (immediateValueRegex.IsMatch(lhs)) {
                registers[target] = Convert.ToUInt16(lhs);
            } else if (operatorRegex.IsMatch(lhs)) {
                Match match = operatorRegex.Match(lhs);

                ushort a = ResolveVariable(match.Groups[1].Value);
                string op = match.Groups[2].Value;
                ushort b = ResolveVariable(match.Groups[3].Value);

                switch (op) {
                    case "AND": registers[target] = (ushort)(a & b); break;
                    case "OR": registers[target] = (ushort)(a | b); break;
                    case "LSHIFT": registers[target] = (ushort)(a << b); break;
                    case "RSHIFT": registers[target] = (ushort)(a >> b); break;
                }
            } else if (notOperatorRegex.IsMatch(lhs)) {
                string source = lhs.Substring(4);
                registers[target] = (ushort)(~(ResolveVariable(source)));
            }
        }
    }

    private ushort GetValue(string key) {
        if (!registers.ContainsKey(key)) {
            registers[key] = 0;
        }
        return registers[key];
    }

    private ushort ResolveVariable(string variable) {
        if (variable.All(char.IsNumber)) {
            return Convert.ToUInt16(variable);
        } else {
            return GetValue(variable);
        }
    }
}

class App {
    static void Main(string[] args) {
        string[] lines = File.ReadAllLines("./input");
        var vm = new VM();
        vm.run(lines);

        foreach(KeyValuePair<string, ushort> entry in vm.registers) {
            Console.WriteLine("" + entry.Key + " <> " + entry.Value);
        }

        Console.WriteLine("Value of a: " + vm.registers["a"]);
    }
}
