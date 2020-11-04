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
using System.Net.Sockets;

namespace Socket_Winform
{
    public partial class Form1 : Form
    {
        static Socket sck;

        public Form1()
        {
            InitializeComponent();
        }

        static public int soc(string st)
        {
            sck = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Parse("192.168.0.42"), 8080);

            try
            {
                sck.Connect(localEndPoint);
            }
            catch
            {
                Console.Write("Unable to connect to remote end point!\r\n");
            }

            byte[] data = Encoding.UTF8.GetBytes(st);

            sck.Send(data);

            Console.Write("Data Sent!\r\n");

            sck.Close();

            return 1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            soc("red_on");
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            soc("red_off");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            soc("blue_on");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            soc("blue_off");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            soc("green_on");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            soc("green_off");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            soc("all_on");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            soc("all_off");
        }
    }
}
