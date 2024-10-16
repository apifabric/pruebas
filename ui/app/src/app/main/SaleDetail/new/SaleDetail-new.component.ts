import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'SaleDetail-new',
  templateUrl: './SaleDetail-new.component.html',
  styleUrls: ['./SaleDetail-new.component.scss']
})
export class SaleDetailNewComponent {
  @ViewChild("SaleDetailForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}