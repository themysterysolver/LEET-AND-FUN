class DiningPhilosophers {
    private Semaphore[] forks;
    private Semaphore mutex;
    public DiningPhilosophers() {
        mutex=new Semaphore(1);
        forks=new Semaphore[5];
        for(int i=0;i<5;i++){
            forks[i]=new Semaphore(1);
        }
    }

    // call the run() method of any runnable to execute its code
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
                            int left=philosopher;
                            int right=(philosopher+1)%5;
                            mutex.acquire();
                            forks[left].acquire();
                            pickLeftFork.run();
                            forks[right].acquire();
                            pickRightFork.run();
                            eat.run();
                            putLeftFork.run();
                            forks[left].release();
                            putRightFork.run();
                            forks[right].release();
                            mutex.release();
    }
}