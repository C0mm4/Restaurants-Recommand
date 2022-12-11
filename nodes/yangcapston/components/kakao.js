import { Map, MapMarker, ZoomControl } from "react-kakao-maps-sdk";
import Styles from "../styles/Home.module.css";
import SearchBox from "./SearchBox";

export default function Kakao() {
  return (
    <div>
      <div className={Styles.KakaomapP}>
        <div className={Styles.Kakaomap}>
          <Map
            center={{ lat: 36.55609600270734, lng: 127.8754074403906 }}
            level={23}
            style={{ width: "100%", height: "280px" }}
          >
            <MapMarker
              position={{ lat: 36.55609600270734, lng: 127.8754074403906 }}
            >
              <div style={{ color: "#000" }}>여기에요!</div>
            </MapMarker>
            <ZoomControl Position="right"></ZoomControl>
          </Map>
        </div>
      </div>
    </div>
  );
}
