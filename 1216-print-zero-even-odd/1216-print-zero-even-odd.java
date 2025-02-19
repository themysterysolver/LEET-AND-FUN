class ZeroEvenOdd {
    private int n,num;
    Semaphore z,s1,s2;
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.num=1;
        z=new Semaphore(1);
        s1=new Semaphore(0);
        s2=new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for(int i=0;i<n;i++){
            z.acquire();
            printNumber.accept(0);
            if(num%2==1)
                s1.release();
            else{
                s2.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for(int i=2;i<=n;i+=2){
            s2.acquire();
            printNumber.accept(this.num);
            num++;
            z.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for(int i=1;i<=n;i+=2){
            s1.acquire();
            printNumber.accept(this.num);
            num++;
            z.release();
        }
    }
}