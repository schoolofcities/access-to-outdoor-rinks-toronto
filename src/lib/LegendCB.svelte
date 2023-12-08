<script>
    $: labels = [
       "General Population",
       "Low Income",
       "Immigrant",
       "Visible Minority",
   ]

   $: title1 = "Demographic Group:"

   $: colour = [
        "#D0D1C9",
        "#1E3765",
        "#6D247A",
        "#007FA3",   
   ]
</script>


<svg width="800" height="30">
   <text class="legend-title" x="0" y="18">{title1} </text>
   <rect
       class="box"
       width="120"
       height="20"
       x="130"
       y="3"
       style="fill:{colour[0]};"
   />
   <rect
       class="box"
       width="120"
       height="20"
       x="252"
       y="3"
       style="fill:{colour[1]};"
   />
   <rect
       class="box"
       width="120"
       height="20"
       x="374"
       y="3"
       style="fill:{colour[2]};"
   />
   <rect
       class="box"
       width="120"
       height="20"
       x="496"
       y="3"
       style="fill:{colour[3]};"
   />
   

   <text class="legend-label" x="135" y="18">{labels[0]}</text>
   <text class="legend-label legend-label-dark" x="278" y="18">{labels[1]}</text>
   <text class="legend-label legend-label-dark" x="405" y="18">{labels[2]}</text>
   <text class="legend-label legend-label-dark" x="511" y="18">{labels[3]}</text>
</svg>


<style>
   p {
       color: var(--brandDarkBlue);
       font-size: 16px;
       font-weight: 400;
       line-height: 24px;
       margin-left: 0px;
       margin-top: 10px;
       margin-right: 0px;
       margin-bottom: 0px;
   }
   .graphTitle {
       color: var(--brandDarkBlue);
       font-size: 16px;
       font-weight: 700;
       line-height: 30px;
       text-decoration: underline;
       margin-left: 0px;
       margin-top: 10px;
       margin-right: 0px;
       margin-bottom: 0px;
   }
   .box {
           stroke-width: 0.5px;
           stroke: rgb(206, 206, 206);
       }
   .legend-label {
           font-size: 13px;
           fill: rgb(0, 0, 0);
       }

   .legend-label-dark {
       font-size: 13px;
       fill: var(--brandWhite)
   }
       
   .legend-title {
           font-family: RobotoRegular;
           font-weight: 600;
           font-size: 13px;
           fill: var(--brandDarkBlue);
           margin-bottom: 0px;
           vertical-align: top;
       }
   </style>