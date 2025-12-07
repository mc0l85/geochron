# Solar Clock Application with Leaflet

A JavaScript application that displays a solar clock with greyline/shading to illustrate areas of darkness throughout the day. The application uses an ESRI base map through Leaflet, updates every 60 seconds, and shows the visitor's location with a green dot.

## Features

- ESRI World Imagery basemap for high-quality satellite imagery
- Accurate greyline/terminator shading showing day/night boundaries using Leaflet.Terminator
- Real-time calculation of solar position
- Geolocation to display the visitor's position with a green dot
- Automatic updates every 60 seconds
- Information panel showing current UTC time and visitor location
- Loading indicators and error handling for better user experience

## Usage

Simply open the `index.html` file in any modern web browser. The application is completely self-contained and doesn't require any additional files or server setup.

When you open the file, you may need to allow location access if you want to see your position on the map. The application will still work without location access, but won't be able to show your position with the green dot.

## Technical Details

### Leaflet Implementation

The application uses Leaflet, a lightweight open-source JavaScript library for interactive maps. Key components:

- Leaflet core library for map display and interaction
- ESRI World Imagery tiles for the base map
- Leaflet.Terminator plugin for day/night visualization
- Leaflet's built-in geolocation capabilities

### Day/Night Visualization

The application uses the Leaflet.Terminator plugin to accurately display the day/night boundary (terminator line). This plugin:

- Calculates the solar position based on the current time
- Creates a polygon representing the night side of Earth
- Updates automatically every 60 seconds

### Geolocation

The application uses the browser's Geolocation API through Leaflet to:

- Detect the visitor's current location
- Display a green dot at that position
- Update the location periodically

## Browser Compatibility

The application should work in all modern browsers, including:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

## Credits

- Map implementation using Leaflet (https://leafletjs.com/)
- Day/night visualization using Leaflet.Terminator (https://github.com/joergdietrich/Leaflet.Terminator)
- Base map tiles from ESRI World Imagery
