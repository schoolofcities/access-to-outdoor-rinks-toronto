<script>
    // https://github.com/schoolofcities/place-and-politics-toronto/blob/467ccdfbb0518cdc3f28669e19cd172c898c9c6b/src/routes/lib/Bar.svelte

    const immigrantTimePrecent = {
        "Under 15 Mins": 19.6,
        "15-30 Mins": 50.9,
        "30-45 Mins": 27.0,
        "45-60 Mins": 1.7,
        "More than 60 Mins": 0.8
    } 

    const lowIncomeTimePercent = {
        "Under 15 Mins": 24.4,
        "15-30 Mins": 50.5,
        "30-45 Mins": 23.8,
        "45-60 Mins": 0.9,
        "More than 60 Mins": 0.3
    }

    const populationTimePercent = {
        "Under 15 Mins": 23.4,
        "15-30 Mins": 51.2,
        "30-45 Mins": 23.1,
        "45-60 Mins": 1.6,
        "More than 60 Mins": 0.7
    }

    const vmTimePercent = {
        "Under 15 Mins": 18.6,
        "15-30 Mins": 49.4,
        "30-45 Mins": 29.0,
        "45-60 Mins": 2.1,
        "More than 60 Mins": 1.0
    }

    const margin = {top:1, bottom:1, left:1, right:1};
    let divWidth;
    const height = 90; 

    $: innerWidth = divWidth-margin.left - margin.right

    

</script>