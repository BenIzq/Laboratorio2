using System;
using static System.IO.StreamReader;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.IO;
using Newtonsoft.Json;
using System.Xml.Schema;
using System.Text.Json;


namespace lab3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            #region Lectura de deserializacion
            string Custom = @"C:\Users\benja\Downloads\input_customer_challenge_lab_3.jsonl";
            string Auctions = @"C:\Users\benja\Downloads\input_auctions_challenge_lab_3.jsonl";

            List<Client> clients = new List<Client>();
            using (StreamReader reader = new StreamReader(Custom))
            {
                while (!reader.EndOfStream)
                {
                    string line = reader.ReadLine();
                    Client client = JsonSerializer.Deserialize<Client>(line);
                    clients.Add(client);
                }
            }

            List<PropertyData> bettors = new List<PropertyData>();
            using (StreamReader reader = new StreamReader(Auctions))
            {
                while (!reader.EndOfStream)
                {
                    string line = reader.ReadLine();
                    PropertyData propertyData = JsonSerializer.Deserialize<PropertyData>(line);
                    bettors.Add(propertyData);
                }
            }
            #endregion

            BinaryTree tree = new BinaryTree();
            foreach (Client client in clients)
            {
                tree.Insert(client);
            }

            foreach (PropertyData propertyData in bettors)
            {
                long winnerDpi;
                List<Tuple<long, int>> dpiBudgetPairs = new List<Tuple<long, int>>();
                List<Customer> orderedCustomers = new List<Customer>();
                foreach (Customer customer in propertyData.Customers)
                {
                    dpiBudgetPairs.Add(new Tuple<long, int>(customer.Dpi, customer.Budget));
                }
                dpiBudgetPairs.Sort((x, y) => y.Item2.CompareTo(x.Item2));
                foreach (Tuple<long, int> pair in dpiBudgetPairs)
                {
                    Customer orderedCustomer = propertyData.Customers.Find(c => c.Dpi == pair.Item1);
                    orderedCustomers.Add(orderedCustomer);
                }
                winnerDpi = Winning(orderedCustomers, propertyData.Rejection);
                Client foundClient = tree.Find(winnerDpi);
                int budget = GetBudget(orderedCustomers, propertyData.Rejection);
                if (foundClient != null)
                {
                    Console.WriteLine($"{{\"dpi\": {foundClient.DPI}, \"budget\": {budget}, \"date\": \"\", \"firstName\": \"{foundClient.FirstName}\",\"lastName\":\"{foundClient.LastName}\", \"birthDate\":\"{foundClient.BirthDate}\",\"job\":\"{foundClient.Job}\",\"placeJob\":\"{foundClient.PlaceJob}\",\"salary\":\"{foundClient.Salary}\",\"property\":\"{propertyData.Property}\"}}");
                }
            }
            Console.ReadLine();
        }

        public static long Winning(List<Customer> customers, int n)
        {
            long winnerDpi = customers[n].Dpi;
            Console.WriteLine(customers[n].Date);
            return winnerDpi;
        }

        public static int GetBudget(List<Customer> customers, int n)
        {
            int budget = customers[n].Budget;
            return budget;
        }
        #region clases generales
        public class Client
    {
        public long DPI { get; set; }
        public string firstName { get; set; }
        public string lastName { get; set; }
        public string birthDate { get; set; }
        public string job { get; set; }
        public string placeJob { get; set; }
        public int salary { get; set; }
    }
    public class PropertyData
    {
        [JsonProperty("property")]
        public string Property { get; set; }

        [JsonProperty("customers")]
        public List<Customer> Customers { get; set; }

        [JsonProperty("rejection")]
        public int Rejection { get; set; }
    }

    public class Customer
    {
        [JsonProperty("dpi")]
        public long Dpi { get; set; }

        [JsonProperty("budget")]
        public int Budget { get; set; }

        [JsonProperty("date")]
        public string Date { get; set; }
    }
}

    internal class ArbolBin
    {
        public NodoArbol Root;
        public void Inserta(Client value)
        {
            Root = Insert(Root, value);
        }

        private NodoArbol Insert(NodoArbol node, Client value)
        {
            if (node == null)
            {
                return new NodoArbol(value);
            }

            if (value.DPI < node.Value.DPI)
            {
                node.Left = Insert(node.Left, value);
            }
            else
            {
                node.Right = Insert(node.Right, value);
            }

            return node;
        }
        public Client Encontrar(long dpi)
        {
            return Find(Root, dpi);
        }

        private Client Find(NodoArbol node, long dpi)
        {
            if (node == null)
            {
                return null;
            }

            if (dpi < node.Value.DPI)
            {
                return Find(node.Left, dpi);
            }
            else if (dpi > node.Value.DPI)
            {
                return Find(node.Right, dpi);
            }
            else
            {
                return node.Value;
            }
        }
    }
#endregion