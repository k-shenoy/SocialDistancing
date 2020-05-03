package com.example.socialdistancing;

import com.google.firebase.database.IgnoreExtraProperties;

@IgnoreExtraProperties
public class Location {

    public double lat, lon, weight;

    public Location() {
        // Default constructor required for calls to DataSnapshot.getValue(User.class)
    }

    public Location(double lat, double lon, double weight) {
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