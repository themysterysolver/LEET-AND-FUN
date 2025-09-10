class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        List<Integer> hCuts = new ArrayList<>();
        for (int cut : horizontalCuts) hCuts.add(cut);
        hCuts.add(0);
        hCuts.add(h);
        Collections.sort(hCuts);

        List<Integer> vCuts = new ArrayList<>();
        for (int cut : verticalCuts) vCuts.add(cut);
        vCuts.add(0);
        vCuts.add(w);
        Collections.sort(vCuts);

        int hmaxi = 0;
        for(int i=0;i<hCuts.size()-1;i++) {
            hmaxi = Math.max(hmaxi,hCuts.get(i + 1) - hCuts.get(i));
        }

        int vmaxi = 0;
        for(int i=0;i<vCuts.size()-1;i++){
            vmaxi = Math.max(vmaxi,vCuts.get(i+1)-vCuts.get(i));
        }
        long mod = 1_000_000_007L;
        return (int)((1L*vmaxi*hmaxi)%mod);
    }
}