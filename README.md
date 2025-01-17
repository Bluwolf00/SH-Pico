<div align="center">
    <h1 align="center">Smart Home Temperature Visualizer
    <br/>
    <br/>
    </h1>
</div>

## Introduction

This project aims to create a web application that displays the room temperature in each room of a house in a graphical interface.

## Technical Overview
> WIP

The hardware side of the project utilises a couple of components:
- 1x RPi Pico - The controller for the connected temperature sensor network and relaying the information to a webserver
- 3x MAX6675 K-Type Thermocouple Sensor - The sensors that will read the ambient room temperature and report it to the Pico.

The Pico will communicate with the thermocouples using the SPI protocol over serial comms. I2C isn't viable due to the modules not having an easy way of changing the hardware address.

A web application will host the graphical interface which will allow the user to view each room's temperature which will be formatted so that a diagram of the floor plan changes colour depending on the temperature of the room.