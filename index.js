function updateMap()
{
    fetch("./data")
    .then(response => response.json())
    .then(rsp =>{
        console.log(rsp.data)
        rsp.data.forEach(element => {
            latitude=element.latitude
            longitude=element.longitude
            cases=element.infected
            if(cases>1000)
            {
                color="rgb(255,0,0)"
            }
            if(cases>5000)
            {
                color="rgb(230,0,0)"
            }
            if(cases>2500)
            {
                color="rgb(200,0,0)"
            }
            if(cases>1000)
            {
                color="rgb(1750,0,0)"
            }
            if(cases>255)
            {
                color="rgb(150,0,0)"
            }
            else
            {
                color="rgb(100,0,0)"
            }
            new mapboxgl.Marker({
                draggable: false,
                color:color
                })
                .setLngLat([longitude,latitude])
                .addTo(map);
        });
    })
}
updateMap();