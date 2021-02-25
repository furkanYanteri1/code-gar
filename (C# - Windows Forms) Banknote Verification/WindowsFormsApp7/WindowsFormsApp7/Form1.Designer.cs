namespace WindowsFormsApp7
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.varyans_textBox = new System.Windows.Forms.TextBox();
            this.test_button = new System.Windows.Forms.Button();
            this.sonuc_label = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.carpiklik_textBox = new System.Windows.Forms.TextBox();
            this.basiklik_textBox = new System.Windows.Forms.TextBox();
            this.entropi_textBox = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // varyans_textBox
            // 
            this.varyans_textBox.Location = new System.Drawing.Point(164, 80);
            this.varyans_textBox.Name = "varyans_textBox";
            this.varyans_textBox.Size = new System.Drawing.Size(110, 26);
            this.varyans_textBox.TabIndex = 0;
            this.varyans_textBox.Text = "Varyans";
            this.varyans_textBox.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // test_button
            // 
            this.test_button.BackColor = System.Drawing.SystemColors.Info;
            this.test_button.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.test_button.ForeColor = System.Drawing.Color.RoyalBlue;
            this.test_button.Location = new System.Drawing.Point(361, 194);
            this.test_button.Name = "test_button";
            this.test_button.Size = new System.Drawing.Size(125, 43);
            this.test_button.TabIndex = 1;
            this.test_button.Text = "Test et!";
            this.test_button.UseVisualStyleBackColor = false;
            this.test_button.Click += new System.EventHandler(this.button1_Click);
            // 
            // sonuc_label
            // 
            this.sonuc_label.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.sonuc_label.AutoSize = true;
            this.sonuc_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.sonuc_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sonuc_label.Location = new System.Drawing.Point(261, 331);
            this.sonuc_label.Name = "sonuc_label";
            this.sonuc_label.Size = new System.Drawing.Size(303, 110);
            this.sonuc_label.TabIndex = 2;
            this.sonuc_label.Text = "--------";
            this.sonuc_label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.sonuc_label.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption;
            this.label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 13F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.Location = new System.Drawing.Point(164, 29);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(529, 32);
            this.label2.TabIndex = 3;
            this.label2.Text = "Aşağıdaki dalgacık dönüşüm bilgilerini giriniz.";
            // 
            // carpiklik_textBox
            // 
            this.carpiklik_textBox.Location = new System.Drawing.Point(301, 80);
            this.carpiklik_textBox.Name = "carpiklik_textBox";
            this.carpiklik_textBox.Size = new System.Drawing.Size(110, 26);
            this.carpiklik_textBox.TabIndex = 4;
            this.carpiklik_textBox.Text = "Çarpıklık";
            this.carpiklik_textBox.TextChanged += new System.EventHandler(this.textBox1_TextChanged_1);
            // 
            // basiklik_textBox
            // 
            this.basiklik_textBox.Location = new System.Drawing.Point(445, 80);
            this.basiklik_textBox.Name = "basiklik_textBox";
            this.basiklik_textBox.Size = new System.Drawing.Size(110, 26);
            this.basiklik_textBox.TabIndex = 5;
            this.basiklik_textBox.Text = "Basıklık";
            this.basiklik_textBox.TextChanged += new System.EventHandler(this.basiklik_textBox_TextChanged);
            // 
            // entropi_textBox
            // 
            this.entropi_textBox.Location = new System.Drawing.Point(583, 80);
            this.entropi_textBox.Name = "entropi_textBox";
            this.entropi_textBox.Size = new System.Drawing.Size(110, 26);
            this.entropi_textBox.TabIndex = 6;
            this.entropi_textBox.Text = "Entropi";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.entropi_textBox);
            this.Controls.Add(this.basiklik_textBox);
            this.Controls.Add(this.carpiklik_textBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.sonuc_label);
            this.Controls.Add(this.test_button);
            this.Controls.Add(this.varyans_textBox);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox varyans_textBox;
        private System.Windows.Forms.Button test_button;
        private System.Windows.Forms.Label sonuc_label;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox carpiklik_textBox;
        private System.Windows.Forms.TextBox basiklik_textBox;
        private System.Windows.Forms.TextBox entropi_textBox;
    }
}

