using System;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Collections.Specialized;

namespace File2Clip
{
    public class App
    {
        [STAThread]
        static void Main(params string[] args)
        {
            StringCollection paths = new StringCollection();
            foreach (string s in args) {
            Console.Write(s);
                paths.Add( 
                    System.IO.Path.IsPathRooted(s) ? 
                      s : 
                      System.IO.Directory.GetCurrentDirectory() + 
                        @"\" + s);
            }
            Clipboard.SetFileDropList(paths);
        }
    }
}
