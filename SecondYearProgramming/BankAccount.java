public class BankAccount
{
    double balance;
    public BankAccount(double b)#Constructor 
    {
        balance = b;
    }
    
    public BankAccount()#Defaultconstructor
    {
        balance = 100.00;
    }
    
    public void withdraw(double w) #method
    {
        balance = balance - w;
    }

    public void deposit(double d) #method
    {
        balance = balance + d;
    }
    
    public String toString() #stringmethod
    {
        return ("The balance is " + balance);
    }

    public void setBalance(double newValue) #setter
    {
        balance = newValue;
    }
    
    public double getBalance() #getter
    {
        return balance;
    }
}

