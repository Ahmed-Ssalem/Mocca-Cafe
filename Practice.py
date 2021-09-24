from tkinter import*
import math,random,os
from tkinter import messagebox

#========= creat app class=============================================


class Bill_App:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1360x700+0+0")
          self.root.title("Billing Software System")
          bg_color="#44494f"
          title=Label(self.root,text="Mocca Cafe",bd=12,relief=GROOVE,bg=bg_color,fg="#ebb639",font=("times new roma",30,"bold"),pady=2).pack(fill=X)
          
          #========= 7. variables ==========================
          #========hot drinkes========
          self.royal_tea=IntVar()
          self.turkish_coffe=IntVar()
          self.nescafe=IntVar()
          self.espresso=IntVar()
          self.mocca=IntVar()
          self.late=IntVar()
          #========fruit juice========
          self.orange=IntVar()
          self.mango=IntVar()
          self.banana=IntVar()
          self.peache=IntVar()
          self.pineapple=IntVar()
          self.mix_fruit=IntVar()
          #========ice cream=========
          self.vanilla=IntVar()
          self.chocolate=IntVar()
          self.mango1=IntVar()
          self.strawberry=IntVar()
          self.nescafe1=IntVar()
          self.oreo=IntVar()
          #========total prices and tax======
          self.hot_price=StringVar()
          self.fruit_price=StringVar()
          self.ice_price=StringVar()
          
          self.hot_tax=StringVar()
          self.fruit_tax=StringVar()
          self.ice_tax=StringVar()
          #======== customer ============
          self.c_name=StringVar()
          self.c_number=StringVar()
          self.bill_no=StringVar()
          x=random.randint(1000,9999)
          self.bill_no.set(str(x))
          self.search_bill=StringVar()
      
          
          
          
          #========= 1. customer details frame ==========================  
          F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="#ebb639",bg=bg_color)
          F1.place(x=0,y=80,relwidth=1)
          
          cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="#dedabb",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
          cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
          
          cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="#dedabb",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
          cphn_txt=Entry(F1,width=15,textvariable=self.c_number,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
          
          c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="#dedabb",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
          c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

          bill_btn=Button(F1,text="search",command=self.find_bill,bg="#972525",fg="white",width=10,bd=5,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


          #========= 2.hot drinks frame ===============================
          F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Hot Drinks",font=("times new roman",15,"bold"),fg="#ebb639",bg=bg_color)
          F2.place(x=5,y=180,width=325,height=380)

          r_tea_lbl=Label(F2,text="Royal Tea",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          r_tea_txt=Entry(F2,width=10,textvariable=self.royal_tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          t_coffe_lbl=Label(F2,text="Turkish Coffe",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          t_coffe_txt=Entry(F2,width=10,textvariable=self.turkish_coffe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          nescafe_lbl=Label(F2,text="Nescafe",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          nescafe_txt=Entry(F2,width=10,textvariable=self.nescafe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          espresso_lbl=Label(F2,text="Espresso",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          espresso_txt=Entry(F2,width=10,textvariable=self.espresso,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          mocca_lbl=Label(F2,text="Mocca",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
          mocca_txt=Entry(F2,width=10,textvariable=self.mocca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          late_lbl=Label(F2,text="Late",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
          late_txt=Entry(F2,width=10,textvariable=self.late,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


          #========= fruit juice frame ===============================
          F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Fruit Juice",font=("times new roman",15,"bold"),fg="#ebb639",bg=bg_color)
          F3.place(x=340,y=180,width=325,height=380)

          orange_lbl=Label(F3,text="Orange",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          orange_txt=Entry(F3,width=10,textvariable=self.orange,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          mango_lbl=Label(F3,text="Mango",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          mango_txt=Entry(F3,width=10,textvariable=self.mango,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          banana_lbl=Label(F3,text="Banana",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          banana_txt=Entry(F3,width=10,textvariable=self.banana,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          peache_lbl=Label(F3,text="Peache",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          peache_txt=Entry(F3,width=10,textvariable=self.peache,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          pineapple_lbl=Label(F3,text="Pineapple",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
          pineapple_txt=Entry(F3,width=10,textvariable=self.pineapple,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          m_fruit_lbl=Label(F3,text="Mix Fruit",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
          m_fruit_txt=Entry(F3,width=10,textvariable=self.mix_fruit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


          #========= 4.ice cream frame ===============================
          F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Ice Cream",font=("times new roman",15,"bold"),fg="#ebb639",bg=bg_color)
          F4.place(x=675,y=180,width=325,height=380)
          
          vanilla_lbl=Label(F4,text="Vanilla",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
          vanilla_txt=Entry(F4,width=10,textvariable=self.vanilla,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          chocolate_lbl=Label(F4,text="Chocolate",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
          chocolate_txt=Entry(F4,width=10,textvariable=self.chocolate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          mango1_lbl=Label(F4,text="Mango",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
          mango1_txt=Entry(F4,width=10,textvariable=self.mango1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          strawberry_lbl=Label(F4,text="Strawberry",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
          strawberry_txt=Entry(F4,width=10,textvariable=self.strawberry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          nascafe1_lbl=Label(F4,text="Nescafe",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
          nescafe1_txt=Entry(F4,width=10,textvariable=self.nescafe1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          oreo_lbl=Label(F4,text="Oreo",bg=bg_color,fg="#dedabb",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
          oreo_txt=Entry(F4,width=10,textvariable=self.oreo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



          #========= 5.bill area ======================================
          F5=Frame(self.root,bd=10,relief=GROOVE)
          F5.place(x=1010,y=180,width=350,height=380)

          bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
          scrol_y=Scrollbar(F5,orient=VERTICAL)
          self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
          scrol_y.pack(side=RIGHT,fill=Y)
          scrol_y.config(command=self.txtarea.yview)       
          self.txtarea.pack(fill=BOTH,expand=1)



          #============ 6.ButtonFrame==================================
          F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="#ebb639",bg=bg_color)
          F6.place(x=0,y=560,relwidth=1,height=140)
          
          m1_lbl=Label(F6,text="Total Hot Drinks Price",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
          m1_txt=Entry(F6,width=18,textvariable=self.hot_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

          m2_lbl=Label(F6,text="Total Fruit Juice Price",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
          m2_txt=Entry(F6,width=18,textvariable=self.fruit_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

          m3_lbl=Label(F6,text="Total Ice Cream Price",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
          m3_txt=Entry(F6,width=18,textvariable=self.ice_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

          m4_lbl=Label(F6,text="Hot Drinks Tax",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
          m4_txt=Entry(F6,width=18,textvariable=self.hot_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

          m5_lbl=Label(F6,text="Fruit Juice Tax",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
          m5_txt=Entry(F6,width=18,textvariable=self.fruit_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

          m6_lbl=Label(F6,text="Ice Cream Tax",bg=bg_color,fg="#dedabb",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
          m6_txt=Entry(F6,width=18,textvariable=self.ice_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


          btn_F=Frame(F6,bd=7,relief=GROOVE)
          btn_F.place(x=740,width=600,height=105)

          total_btn=Button(btn_F,command=self.total,text="Total",bg="#972525",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
          Gbill_btn=Button(btn_F,text="Print Bill",command=self.bill_area,bg="#972525",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
          Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="#972525",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
          Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="#972525",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        
          self.welcome_bill()

    def total(self):
        
        self.h_r_t_p=self.royal_tea.get()*12
        self.h_t_c_p=self.turkish_coffe.get()*15
        self.h_n_p=self.nescafe.get()*21
        self.h_e_p=self.espresso.get()*18
        self.h_m_p=self.mocca.get()*23
        self.h_l_p=self.late.get()*25
        
        self.total_hot_price=float(           
                                self.h_r_t_p+
                                self.h_t_c_p+
                                self.h_n_p+
                                self.h_e_p+
                                self.h_m_p+        
                                self.h_l_p
                                )
        self.hot_price.set(str(self.total_hot_price))
        self.h_tax=round((self.total_hot_price*0.1),2)
        self.hot_tax.set(str(self.h_tax))          
           

        self.f_o_p=self.orange.get()*20
        self.f_m_p=self.mango.get()*25
        self.f_b_p=self.banana.get()*25
        self.f_p_p=self.peache.get()*25
        self.f_pi_p=self.pineapple.get()*25
        self.f_m_f_p=self.mix_fruit.get()*35
        
        self.total_fruit_price=float(           
                                self.f_o_p+
                                self.f_m_p+
                                self.f_b_p+
                                self.f_p_p+
                                self.f_pi_p+     
                                self.f_m_f_p
                                )
        self.fruit_price.set(str(self.total_fruit_price))
        self.f_tax=round((self.total_fruit_price*0.1),2)
        self.fruit_tax.set(str(self.f_tax))         

        self.i_v_p=self.vanilla.get()*15
        self.i_c_p=self.chocolate.get()*15
        self.i_m1_p=self.mango1.get()*17
        self.i_s_p=self.strawberry.get()*17
        self.i_n1_p=self.nescafe1.get()*15
        self.i_o1_p=self.oreo.get()*20
        
        self.total_ice_price=float(           
                                self.i_v_p+
                                self.i_c_p+
                                self.i_m1_p+
                                self.i_s_p+
                                self.i_n1_p+  
                                self.i_o1_p                       
                                )
        self.ice_price.set(str(self.total_ice_price))           
        self.i_tax=round((self.total_ice_price*0.1),2)
        self.ice_tax.set(str(self.i_tax)) 
        
        self.Total_bill=float(  self.total_hot_price+
                                self.total_fruit_price+
                                self.total_ice_price+
                                self.h_tax+
                                self.f_tax+
                                self.i_tax
                             )

    def welcome_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\twelcome in mocca caf�\n")     
        self.txtarea.insert(END,f"\n Bill Number :  {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name :  {self.c_name.get()}")                    
        self.txtarea.insert(END,f"\n Phone Nomber :  {self.c_number.get()}")            
        self.txtarea.insert(END,"\n======================================")  
        self.txtarea.insert(END,f"\n product\t\tQTY\t\tprice")
        self.txtarea.insert(END,"\n======================================")        
        
                      
                                    
                                                                
    def bill_area(self):
        if self.hot_price.get()=="0.0" and self.fruit_price.get()=="0.0" and self.ice_price.get()=="0.0":
            messagebox.showerror("Error","No Products entered")
        else:

            self.welcome_bill()
        
     #=======hot drinkes ====
            if self.royal_tea.get()!=0:
                 self.txtarea.insert(END,f"\n Royal Tea\t\t{self.royal_tea.get()}\t\t{self.h_r_t_p}")
            if self.turkish_coffe.get()!=0:
                 self.txtarea.insert(END,f"\n Turkish Coffe\t\t{self.turkish_coffe.get()}\t\t{self.h_t_c_p}")        
            if self.nescafe.get()!=0:
                 self.txtarea.insert(END,f"\n Nescaf�\t\t{self.nescafe.get()}\t\t{self.h_n_p}")        
            if self.espresso.get()!=0:
                 self.txtarea.insert(END,f"\n Espresso\t\t{self.espresso.get()}\t\t{self.h_e_p}")               
            if self.mocca.get()!=0:
                 self.txtarea.insert(END,f"\n Mocca\t\t{self.mocca.get()}\t\t{self.h_m_p}")
            if self.late.get()!=0:
                 self.txtarea.insert(END,f"\n late\t\t{self.late.get()}\t\t{self.h_l_p}")
             
     #=======fruit juice====
            if self.orange.get()!=0:
                 self.txtarea.insert(END,f"\n Orange Juice\t\t{self.orange.get()}\t\t{self.f_o_p}")
            if self.mango.get()!=0:
                 self.txtarea.insert(END,f"\n Mango Juice\t\t{self.mango.get()}\t\t{self.f_m_p}")        
            if self.banana.get()!=0:
                 self.txtarea.insert(END,f"\n Banana Juice\t\t{self.banana.get()}\t\t{self.f_b_p}")        
            if self.peache.get()!=0:
                 self.txtarea.insert(END,f"\n Peache Juice\t\t{self.peache.get()}\t\t{self.f_p_p}")               
            if self.pineapple.get()!=0:
                 self.txtarea.insert(END,f"\n Pineapple Juice\t\t{self.pineapple.get()}\t\t{self.f_pi_p}")
            if self.mix_fruit.get()!=0:
                 self.txtarea.insert(END,f"\n Mix Fruit\t\t{self.mix_fruit.get()}\t\t{self.f_m_f_p}")
             
     #=======ice cream ====
            if self.vanilla.get()!=0:
                 self.txtarea.insert(END,f"\n Vanilla I.C\t\t{self.vanilla.get()}\t\t{self.i_v_p}")
            if self.chocolate.get()!=0:
                 self.txtarea.insert(END,f"\n Chocolate I.C\t\t{self.chocolate.get()}\t\t{self.i_c_p}")
            if self.mango1.get()!=0:
                 self.txtarea.insert(END,f"\n Mango I.C\t\t{self.mango1.get()}\t\t{self.i_m1_p}")    
            if self.strawberry.get()!=0:
                 self.txtarea.insert(END,f"\n Strawberry I.C\t\t{self.strawberry.get()}\t\t{self.i_s_p}")               
            if self.nescafe1.get()!=0:
                 self.txtarea.insert(END,f"\n Nescafe I.C\t\t{self.nescafe1.get()}\t\t{self.i_n1_p}")
            if self.oreo.get()!=0:
                 self.txtarea.insert(END,f"\n Oreo I.C\t\t{self.oreo.get()}\t\t{self.i_o1_p}")
             
            self.txtarea.insert(END,"\n--------------------------------------")  
            if self.hot_tax.get()!="0.0":
                 self.txtarea.insert(END,f"\n Hot Drinks Tax\t\t\t\t{self.hot_tax.get()}")
            if self.fruit_tax.get()!="0.0":
                 self.txtarea.insert(END,f"\n Fruit Juice Tax\t\t\t\t{self.fruit_tax.get()}")
            if self.ice_tax.get()!="0.0":
                 self.txtarea.insert(END,f"\n Ice Cream Tax\t\t\t\t{self.ice_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill : \t\t\t\t{self.Total_bill}")   
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.save_bill()
       
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1= open("C:/Users/Kimo Store/source/repos/practice/bills_data/"+str(self.bill_no.get())+".txt","w",encoding='utf-8')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("C:/Users/Kimo Store/source/repos/practice/bills_data/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C:/Users/Kimo Store/source/repos/practice/bills_data/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="Yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
         op=messagebox.askyesno("Clear","Do you really want to clear ?")
         if op>0:
            self.royal_tea.set(0)
            self.turkish_coffe.set(0)
            self.nescafe.set(0)
            self.espresso.set(0)
            self.mocca.set(0)
            self.late.set(0)
         #========fruit juice========
            self.orange.set(0)
            self.mango.set(0)
            self.banana.set(0)
            self.peache.set(0)
            self.pineapple.set(0)
            self.mix_fruit.set(0)
        #========ice cream=========
            self.vanilla.set(0)
            self.chocolate.set(0)
            self.mango1.set(0)
            self.strawberry.set(0)
            self.nescafe1.set(0)
            self.oreo.set(0)
       #========total prices and tax======
            self.hot_price.set("")
            self.fruit_price.set("")
            self.ice_price.set("")   
            self.hot_tax.set("")
            self.fruit_tax.set("")
            self.ice_tax.set("")
      #======== customer ============
            self.c_name.set("")
            self.c_number.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit ?")
        if op>0:
            self.root.destroy()


root =Tk()
obj = Bill_App(root)
root.mainloop()















