class Solution {
    public double calculateIncreaseInPassRatio(double pass,double total){
        return ((double)(pass+1)/(total+1))-((double)pass/total);
    }
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<double[]> heap=new PriorityQueue<>((a,b)->Double.compare(b[0],a[0]));
        for(int[] cl:classes){
            double pass=cl[0],total=cl[1];
            heap.offer(new double[]{calculateIncreaseInPassRatio(pass,total),pass,total});
        }
        for(int i=0;i<extraStudents;i++){
            double[] top=heap.poll();
            double pass=top[1],total=top[2];
            heap.offer(new double[]{calculateIncreaseInPassRatio(pass+1,total+1),pass+1,total+1});
        }
        double avg=0;
        while(!heap.isEmpty()){
            double[] top=heap.poll();
            double pass=top[1],total=top[2];
            avg+=((double)pass)/total;
        }
        return avg/classes.length;
    }
}