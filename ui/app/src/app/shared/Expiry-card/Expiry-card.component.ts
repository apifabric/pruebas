import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Expiry-card.component.html',
  styleUrls: ['./Expiry-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Expiry-card]': 'true'
  }
})

export class ExpiryCardComponent {


}