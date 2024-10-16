import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SaleDetail-card.component.html',
  styleUrls: ['./SaleDetail-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SaleDetail-card]': 'true'
  }
})

export class SaleDetailCardComponent {


}