class Foo {
    private boolean oneDone,twoDone;
    public Foo() {
        oneDone=false;
        twoDone=false;
    }
    public synchronized void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        oneDone=true;
        notifyAll();
    }

    public synchronized void second(Runnable printSecond) throws InterruptedException {
        while(!oneDone){
            wait();
        }
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        twoDone=true;
        notifyAll();
    }
    public synchronized void third(Runnable printThird) throws InterruptedException {
        while(!twoDone){
            wait();
        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}