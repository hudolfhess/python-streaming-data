using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace ConsumingApiMPWithSocket
{
    class MainClass
    {
        //static string host = "172.16.50.144";
        static string host = "172.16.50.144";
        static int port = 8080;

        private static Socket ConnectSocket()
        {
            var ipe = new IPEndPoint(IPAddress.Parse(host), port);
            var socket = new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            socket.Connect(ipe);

            if (!socket.Connected)
            {
                //TODO: raise
            }

            return socket;
        }

        private static string ReceiveModel(string model)
        {
            var socket = ConnectSocket();

            var bytesSent = Encoding.ASCII.GetBytes(model);
            socket.Send(bytesSent, bytesSent.Length, 0);

            int bytes = 0;
            string content = string.Empty;
            var bytesReceived = new byte[4096];
            do
            {
                bytes = socket.Receive(bytesReceived, bytesReceived.Length, 0);
                content = content + Encoding.ASCII.GetString(bytesReceived, 0, bytes);
            }
            while (bytes > 0);

            return content;
        }

        public static void Main(string[] args)
        {
            var models = new List<string> { "produtos", "clientes" };
            foreach (var model in models)
            {
                Task.Run(() =>
                {
                    string result = ReceiveModel(model);
                    Console.WriteLine(result);
                });
            }
        }
    }
}
