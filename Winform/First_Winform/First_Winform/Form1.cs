using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.IO;

namespace First_Winform
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/red_on");

            Console.WriteLine(reply);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/blue_on");

            Console.WriteLine(reply);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/blue_off");

            Console.WriteLine(reply);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/green_on");

            Console.WriteLine(reply);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/green_off");

            Console.WriteLine(reply);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/all_on");

            Console.WriteLine(reply);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/all_off");

            Console.WriteLine(reply);
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            WebClient client = new WebClient();
            string reply = client.DownloadString("http://192.168.0.42:8080/red_off");

            Console.WriteLine(reply);
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}