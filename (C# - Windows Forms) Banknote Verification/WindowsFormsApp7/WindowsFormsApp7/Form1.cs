using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (float.Parse(varyans_textBox.Text) > 1.744)
            {
                if (float.Parse(basiklik_textBox.Text) > -4.959)
                {
                    if (float.Parse(basiklik_textBox.Text) > -4.802)
                    {
                        if (float.Parse(varyans_textBox.Text) > 2.037)
                        {
                            sonuc_label.BackColor = Color.Red;
                            sonuc_label.Text = "SAHTE";
                        }
                        else
                        {
                            sonuc_label.BackColor = Color.Red;
                            sonuc_label.Text = "SAHTE";
                        }
                    }
                    else
                    {
                        if (float.Parse(varyans_textBox.Text) > 3.2222)
                        {
                            sonuc_label.BackColor = Color.Red;
                            sonuc_label.Text = "SAHTE";
                        }
                        else
                        {
                            sonuc_label.BackColor = Color.Green;
                            sonuc_label.Text = "GERCEK";
                        }
                    }
                }
                else
                {
                    sonuc_label.BackColor = Color.Green;
                    sonuc_label.Text = "GERCEK";
                }
            }
            else 
            {
                if (float.Parse(carpiklik_textBox.Text) > 9.675)
                {
                    sonuc_label.BackColor = Color.Red;
                    sonuc_label.Text = "SAHTE";
                }
                else 
                {
                    if (float.Parse(varyans_textBox.Text) > -0.403)
                    {
                        if (float.Parse(basiklik_textBox.Text) > -3.847)
                        {
                            sonuc_label.BackColor = Color.Red;
                            sonuc_label.Text = "SAHTE";
                        }
                        else
                        {
                            sonuc_label.BackColor = Color.Green;
                            sonuc_label.Text = "GERCEK";
                        }
                    }
                    else 
                    {
                        if (float.Parse(basiklik_textBox.Text) > -3.697)
                        {
                            sonuc_label.BackColor = Color.Green;
                            sonuc_label.Text = "GERCEK";
                        }
                        else 
                        {
                            sonuc_label.BackColor = Color.Red;
                            sonuc_label.Text = "SAHTE";
                        }
                    }
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void basiklik_textBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
