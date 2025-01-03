class H2O {
    private Semaphore h,o;
    private CyclicBarrier b;
    public H2O() {
        h=new Semaphore(2);
        o=new Semaphore(1);
        b=new CyclicBarrier(3);
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		h.acquire();
        try{
            b.await();
        }catch(Exception e){
            System.out.println(e.getMessage());
        }
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        h.release();
        
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        o.acquire();
        try{
            b.await();
        }catch(Exception e){
            System.out.println(e.getMessage());
        }
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
        o.release();
    }
}
