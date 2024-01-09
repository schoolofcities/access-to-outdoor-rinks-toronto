<script>
     $: labels = [
        "<15",
        "15-30",
        "30-45",
        "45-60",
        ">60"
    ]

    $: title1 = "Travel Time to the Nearest Outdoor Skating Rink"

    $: colour = [
        "#f1eef6",
        "#bdc9e1",
        "#74a9cf",
        "#2b8cbe",
        "#045a8d"
    ]
</script>


<svg width="350" height="50">
    <text class="legend-title" x="0" y="18">{title1} </text>
    <rect
        class="box"
        width="45"
        height="20"
        x="1"
        y="30"
        style="fill:{colour[0]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="50"
        y="30"
        style="fill:{colour[1]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="100"
        y="30"
        style="fill:{colour[2]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="150"
        y="30"
        style="fill:{colour[3]};"
    />
    <rect
        class="box"
        width="45"
        height="20"
        x="200"
        y="30"
        style="fill:{colour[4]};"
    />

    <text class="legend-label" x="14" y="45">{labels[0]}</text>
	<text class="legend-label" x="56" y="45">{labels[1]}</text>
	<text class="legend-label" x="106" y="45">{labels[2]}</text>
	<text class="legend-label legend-label-dark" x="156" y="45">{labels[3]}</text>
	<text class="legend-label legend-label-dark" x="210" y="45">{labels[4]}</text>

    <text class="legend-label legend-label-minutes" x="250" y="45" color="red">minutes</text>

</svg>


<style>

    .box {
            stroke-width: 0.5px;
            stroke: rgb(206, 206, 206);
        }
    .legend-label {
            font-size: 13px;
            fill: rgb(0, 0, 0);
        }

    .legend-label-minutes {
        font-size: 13px;
        fill: var(--brandDarkBlue);
    }


    .legend-label-dark {
        font-size: 13px;
        fill: var(--brandWhite)
    }
        
    .legend-title {
            font-family: RobotoBold;
            /* font-weight: 600; */
            font-size: 16px;
            fill: var(--brandDarkBlue);
            margin-bottom: 0px;
            vertical-align: top;
        }
    </style>
