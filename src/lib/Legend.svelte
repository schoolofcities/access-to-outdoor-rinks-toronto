<script>
     $: labels = [
        "<15",
        "15-30",
        "30-45",
        "45-60",
        "<60"
    ]

    $: title1 = "Travel Time (minutes)"

    $: colour = [
        "#f1eef6",
        "#bdc9e1",
        "#74a9cf",
        "#2b8cbe",
        "#045a8d"
    ]
</script>


<svg width="300" height="75">
    <text class="legend-title" x="0" y="20">{title1} </text>
    <rect
        class="box"
        width="45"
        height="20"
        x="0"
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

    <text class="legend-label" x="10" y="65">{labels[0]}</text>
	<text class="legend-label" x="56" y="65">{labels[1]}</text>
	<text class="legend-label" x="106" y="65">{labels[2]}</text>
	<text class="legend-label" x="156" y="65">{labels[3]}</text>
	<text class="legend-label" x="210" y="65">{labels[4]}</text>

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
    .legend-title {
            font-family: RobotoRegular;
            font-size: 13px;
            fill: var(--brandDarkBlue);
            margin-bottom: 0px;
            vertical-align: top;
        }
    </style>
