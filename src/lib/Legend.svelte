<script>
     $: labels = [
        "<15",
        "15-30",
        "30-45",
        "45-60",
        ">60"
    ]

    $: title1 = "Travel Time (Minutes):"

    $: colour = [
        "#f1eef6",
        "#bdc9e1",
        "#74a9cf",
        "#2b8cbe",
        "#045a8d"
    ]
</script>


<svg width="500" height="30">
    <text class="legend-title" x="0" y="18">{title1} </text>
    <rect
        class="box"
        width="45"
        height="20"
        x="140"
        y="3"
        style="fill:{colour[0]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="190"
        y="3"
        style="fill:{colour[1]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="240"
        y="3"
        style="fill:{colour[2]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="290"
        y="3"
        style="fill:{colour[3]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="340"
        y="3"
        style="fill:{colour[4]};"
    />

    <text class="legend-label" x="150" y="18">{labels[0]}</text>
	<text class="legend-label" x="196" y="18">{labels[1]}</text>
	<text class="legend-label" x="246" y="18">{labels[2]}</text>
	<text class="legend-label legend-label-dark" x="296" y="18">{labels[3]}</text>
	<text class="legend-label legend-label-dark" x="350" y="18">{labels[4]}</text>

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
            fill: rgb(66, 66, 66);
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
