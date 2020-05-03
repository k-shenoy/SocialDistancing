package com.example.socialdistancing;

import com.google.firebase.database.IgnoreExtraProperties;

@IgnoreExtraProperties
public class Locations {

    public double lat, lon, weight;

    public Locations() {
        // Default constructor required for calls to DataSnapshot.getValue(User.class)
    }

    public Locations(double lat, double lon, double weight) {
        this.lat = lat;
        this.lon = lon;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Locations{" +
                "lat=" + lat +
                ", lon=" + lon +
                ", weight=" + weight +
                '}';
    }
}