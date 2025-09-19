class Spreadsheet {
    private Map<String,Integer> hash;
    private int r;
    public Spreadsheet(int rows) {
        this.hash = new HashMap<>();
        this.r = rows; 
    }
    
    public void setCell(String cell, int value) {
        hash.put(cell,value);
    }
    
    public void resetCell(String cell) {
        hash.put(cell,0);
    }
    
    public int getValue(String formula) {
        String x = formula.substring(1);
        String[] arr = x.split("\\+");
        String a = arr[0]; String b = arr[1];
        int ans = 0;
        if(a.matches("\\d+")) ans+=Integer.parseInt(a);
        if(b.matches("\\d+")) ans+=Integer.parseInt(b);
        if(hash.containsKey(a)) ans+=hash.get(a);
        if(hash.containsKey(b)) ans+=hash.get(b);
        return ans;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */