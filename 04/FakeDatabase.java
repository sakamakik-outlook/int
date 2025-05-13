import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class FakeDatabase {

    FakeDatabase() {
        // Constructor
    }
    private int value = 0;

    public synchronized void update(String name) {
        System.out.println("Thread " + name + ": starting update");
        int localCopy = value;
        localCopy += 1;
        try {
            Thread.sleep(2000); // Simulate long-running operation
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        value = localCopy;
        System.out.println("Thread " + name + ": finishing update");
    }

    public int getValue() {
        return value;
    }

    public static void main(String[] args) {
        FakeDatabase database = new FakeDatabase();
        System.out.println("Testing update. Starting value is " + database.getValue());

        ExecutorService executor = Executors.newFixedThreadPool(2);
        for (int i = 0; i < 2; i++) {
            final int index = i;
            executor.submit(() -> database.update(String.valueOf(index)));
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
            // wait for all tasks to finish
        }

        System.out.println("Testing update. Ending value is " + database.getValue());
    }
}
