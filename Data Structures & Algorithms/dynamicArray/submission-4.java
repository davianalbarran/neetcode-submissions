class DynamicArray {
    private int[] storage;
    private int numOfItems;

    public DynamicArray(int capacity) {
        this.storage = new int[capacity];
    }

    public int get(int i) {
        return storage[i];
    }

    public void set(int i, int n) {
        storage[i] = n;
    }

    public void pushback(int n) {
        if (getSize() == getCapacity()) resize();

        storage[getSize()] = n;
        numOfItems++;
    }

    public int popback() {
        numOfItems--;
        int val = storage[getSize()];
        storage[getSize()] = 0;
        return val;
    }

    private void resize() {
        int[] tempStorage = new int[storage.length*2];

        for (int i = 0; i < storage.length; i++) {
            tempStorage[i] = storage[i];
        }

        storage = tempStorage;
    }

    public int getSize() {
        return numOfItems;
    }

    public int getCapacity() {
        return storage.length;
    }
}
