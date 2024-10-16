import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Expiry-new',
  templateUrl: './Expiry-new.component.html',
  styleUrls: ['./Expiry-new.component.scss']
})
export class ExpiryNewComponent {
  @ViewChild("ExpiryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}