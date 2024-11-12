class Solution {
    public double angleClock(int hour, int minutes) {
        double minAngle=minutes*6;
        double hrsAngle=(hour%12)*30+(minutes/60.0)*30;
        double angle=Math.abs(hrsAngle-minAngle);
        return Math.min(360-angle,angle);
    }
}