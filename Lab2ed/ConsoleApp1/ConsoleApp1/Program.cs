using System;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Collections.Generic;

public class Program
{
    public class House
    {
        [JsonPropertyName("zoneDangerous")]
        public string ZoneDangerous { get; set; }
        
        [JsonPropertyName("address")]
        public string Address { get; set; }
        
        [JsonPropertyName("price")]
        public double Price { get; set; }
        
        [JsonPropertyName("contactPhone")]
        public string ContactPhone { get; set; }
        
        [JsonPropertyName("id")]
        public string Id { get; set; }
    }
    
    public class Apartment
    {
        [JsonPropertyName("isPetFriendly")]
        public bool IsPetFriendly { get; set; }
        
        [JsonPropertyName("address")]
        public string Address { get; set; }
        
        [JsonPropertyName("price")]
        public double Price { get; set; }
        
        [JsonPropertyName("contactPhone")]
        public string ContactPhone { get; set; }
        
        [JsonPropertyName("id")]
        public string Id { get; set; }
    }
    
    public class Premise
    {
        [JsonPropertyName("commercialActivities")]
        public string[] CommercialActivities { get; set; }
        
        [JsonPropertyName("address")]
        public string Address { get; set; }
        
        [JsonPropertyName("price")]
        public double Price { get; set; }
        
        [JsonPropertyName("contactPhone")]
        public string ContactPhone { get; set; }
        
        [JsonPropertyName("id")]
        public string Id { get; set; }
    }
    
    public class Builds
    {
        [JsonPropertyName("Premises")]
        public Premise[] Premises { get; set; }
        
        [JsonPropertyName("Apartments")]
        public Apartment[] Apartments { get; set; }
        
        [JsonPropertyName("Houses")]
        public House[] Houses { get; set; }
    }
    
    public class Input1
    {
        [JsonPropertyName("services")]
        public Dictionary<string, bool> Services { get; set; }
        
        [JsonPropertyName("builds")]
        public Builds Builds { get; set; }
    }
    
    public class Input2
    {
        [JsonPropertyName("budget")]
        public double Budget { get; set; }
        
        [JsonPropertyName("typeBuilder")]
        public string TypeBuilder { get; set; }
        
        [JsonPropertyName("requiredServices")]
        public string[] RequiredServices { get; set; }
        
        [JsonPropertyName("commercialActivity")]
        public string CommercialActivity { get; set; }
        
        [JsonPropertyName("wannaPetFriendly")]
        public bool WannaPetFriendly { get; set; }
        
        [JsonPropertyName("minDanger")]
        public string MinDanger { get; set; }
    }
    
    public class InputLab
    {
        [JsonPropertyName("input1")]
        public Input1[] Input1 { get; set; }
        
        [JsonPropertyName("input2")]
        public Input2 Input2 { get; set; }
    }

    static void Main(string[] args)
    {
        for(int r = 0; r < 100; r++)
        {
            string jsonText = File.ReadAllText(@"D:\Universidad Rafael Landìvar\6to Ciclo 2023\Estructura de Datos I\input_challenge_lab_2.jsonl");
            string[] jsonObjects = jsonText.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);
            InputLab input = JsonSerializer.Deserialize<InputLab>(jsonObjects[r
